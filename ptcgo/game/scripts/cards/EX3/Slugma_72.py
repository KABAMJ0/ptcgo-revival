from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.support_common import gust_then

async def burn_new_defender(ctx, pokemon):
    await ctx.apply_special_condition(pokemon, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="1b679fba-8c96-5cae-be84-d6938016b739",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Luring Flame",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. The new Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=gust_then(burn_new_defender, opponent_chooses=True),
        ),
    ],
)