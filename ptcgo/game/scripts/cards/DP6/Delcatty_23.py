from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard, on_bench


async def _attracting_body(ctx):
    attacker = getattr(ctx, "damaged_by", None)
    if attacker is None or attacker.owning_player_id == ctx.player_id:
        return
    results = await ctx.flip_coins(1, "Attracting Body")
    if results and results[0]:
        await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="23149dd4-dfb6-5796-8814-a77de41d2b3e",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Attracting Body",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            game_text="If Delcatty is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Delcatty is Knocked Out), flip a coin. If heads, the Attacking Pok\u00e9mon is now Confused.",
            effect=_attracting_body,
        ),
        Attack(
            title="Energy Assist",
            game_text="Search your discard pile for a basic Energy card and attach it to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target=on_bench),
        ),
    ],
)