from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.content.definitions import Activations
from ptcgo.game.session.passives import is_basic_energy

def _basic_fire_in_hand(board, player_id, pokemon):
    area = board.find_player_area(player_id, "hand")
    return any(is_basic_energy(card)
               and energy_provides_type(card, PokemonTypes.FIRE.value)
               for card in (area.children if area else []))


async def _torrid_scales(ctx):
    options = [card for card in ctx.hand() if is_basic_energy(card)
               and energy_provides_type(card, PokemonTypes.FIRE.value)]
    if not options:
        return
    picks = await ctx.choose_cards(
        options, 1, minimum=1,
        prompt="Discard a Basic Fire Energy card from your hand")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.apply_special_condition(ctx.opponent_active(),
                                      SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="4d42b5df-a6a2-5662-acf9-fc5b9ee91281",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Ability(
            title="Torrid Scales",
            game_text="You must discard a Basic Fire Energy card from your hand in order to use this Ability. Once during your turn, you may make your opponent's Active Pok\u00e9mon Burned.",
            effect=_torrid_scales,
            activation=Activations.ONCE_PER_TURN,
            condition=_basic_fire_in_hand,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)