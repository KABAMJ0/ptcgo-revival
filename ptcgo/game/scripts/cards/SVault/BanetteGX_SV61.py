from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard

from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import Activations


async def shady_move(ctx):
    """Move 1 damage counter from any Pokemon in play to any other."""
    if not await ctx.ask_yes_no("Move 1 damage counter to another Pokemon?"):
        return
    pool = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    damaged = [p for p in pool if ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0) > 0]
    if not damaged:
        return
    source = await ctx.choose_pokemon(damaged, "Choose a damaged Pokemon to take a counter from")
    if source is None:
        return
    await ctx.move_damage_counters(
        source, [p for p in pool if p is not source], max_count=1,
        prompt="Place the moved damage counter on another Pokemon")

card = PokemonCardDef(
    guid="9c1eb693-20a3-5ae0-a1ac-1e1defea1eac",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BanetteGX.Name",
    display_name="Banette-GX",
    searchable_by=["Banette-GX", "Stage 1", "GX", "BanetteGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=61,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Shady Move",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may move 1 damage counter from 1 Pok\u00e9mon to another Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=shady_move,
        ),
        Attack(
            title="Shadow Chant",
            game_text="This attack does 10 more damage for each Supporter card in your discard pile. You can't add more than 100 damage in this way.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Tomb Hunt-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=recover_from_discard(count=3),
        ),
    ],
)