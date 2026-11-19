from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack
from ptcgo.game.session.effects import is_special_energy


async def psyjamming(ctx) -> None:
    """Shuffle the opponent's Special Energy around their own Pokemon."""
    theirs = ctx.opponent_pokemon_in_play()
    await ctx.move_energy_freely(
        theirs, theirs, predicate=is_special_energy, max_count=None,
        prompt="Choose a Special Energy to move",
    )


card = PokemonCardDef(
    guid="803fdafe-3930-5313-8f49-23fdb698d118",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    display_name="Azelf",
    searchable_by=["Azelf", "Basic", "Azelf"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=482,
    abilities=[
        Attack(
            title="Trading Places",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=switch_self_attack(),
        ),
        Attack(
            title="Psyjamming",
            game_text="Move as many Special Energy attached to your opponent's Pok\u00e9mon to your opponent's other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=psyjamming,
        ),
    ],
)