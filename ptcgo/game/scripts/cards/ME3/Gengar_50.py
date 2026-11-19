from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.data_utils import Triggers


async def persistent_cells(ctx):
    """Knocked out by an opponent's attack: return to hand instead of the
    discard pile (attached cards are discarded normally)."""
    if not ctx.ko_from_attack:
        return
    await ctx.put_in_hand([ctx.source], reveal=False)


card = PokemonCardDef(
    guid="033ddd56-cbc3-5560-afa1-6a9768f483ef",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=50,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Infinite Shadow",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, put it into your hand instead of the discard pile. (Discard all attached cards.)",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=persistent_cells,
        ),
        Attack(
            title="Mind Jack",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), per=30, base=10),
        ),
    ],
)