from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def energy_control(ctx):
    """Flip a coin; on heads move one basic Energy between two of the
    opponent's Pokemon."""
    heads = await ctx.flip_coins(1, ctx.ability.title)
    if not (heads and heads[0]):
        return
    theirs = [pokemon for pid in ctx.board.player_ids if pid != ctx.player_id
              for pokemon in ctx.board.pokemon_in_play(pid)]
    holders = [pokemon for pokemon in theirs
               if any(is_basic_energy_card(card)
                      for card in ctx.attached_energies(pokemon))]
    if len(theirs) < 2 or not holders:
        return
    await ctx.move_energy_freely(
        holders, theirs, predicate=is_basic_energy_card, max_count=1,
        prompt="Choose a basic Energy card to move")


card = PokemonCardDef(
    guid="ae4d162b-f27a-5ec7-ae63-b171ca9c13b1",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Control",
            game_text="Flip a coin. If heads, choose a basic Energy card attached to 1 of your opponent's Pok\u00e9mon and attach it to another of your opponent's Pok\u00e9mon of your choice.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_control,
        ),
        Attack(
            title="Telekinesis",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=snipe_attack(30, pool="any"),
        ),
    ],
)