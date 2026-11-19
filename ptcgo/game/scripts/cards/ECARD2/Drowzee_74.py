from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import gust_then
from ptcgo.game.attributes import SpecialConditions


async def _asleep_rider(ctx, new_active):
    await ctx.apply_special_condition(new_active, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="e60793a7-3d0e-5cce-b59c-24cf9648d1c5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic", "Drowzee"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Attack(
            title="Sleep Inducer",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Benched Pok\u00e9mon and switch the Defending Pok\u00e9mon with it. The new Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=flip_gate(gust_then(_asleep_rider, opponent_chooses=False)),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)