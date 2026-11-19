from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                   SpecialConditions)
from ptcgo.game.card_effects.support_common import gust_then


card = PokemonCardDef(
    guid="37bbfdde-b51d-5b3d-ba27-a23422f3e125",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1", "Roserade"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Attack(
            title="Inviting Poison",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. The new Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=gust_then(lambda ctx, active: ctx.apply_special_condition(
                active, SpecialConditions.POISONED)),
        ),
        Attack(
            title="Flower Tornado",
            game_text="Move any number of Grass Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)