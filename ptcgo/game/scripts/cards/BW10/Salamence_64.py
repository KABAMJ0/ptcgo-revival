from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack, \
    on_evolve
from ptcgo.game.data_utils import Triggers


async def _breakwing_discard(ctx) -> None:
    tools = [tool for tool, holder in ctx.tools_in_play()
             if holder.owning_player_id != ctx.player_id
             and not ctx.effects_blocked(holder)]
    if tools:
        await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="7439e91f-6929-55ff-888c-3b255d54f126",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence",
    searchable_by=["Salamence", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=64,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Breakwing",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may discard all Pok\u00e9mon Tool cards attached to each of your opponent's Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=on_evolve(_breakwing_discard),
        ),
        Attack(
            title="Gaia Crush",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=discard_stadium_attack(),
        ),
    ],
)