from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f40b08e7-5ecc-514b-9938-7231a237c638",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    display_name="Smoliv",
    searchable_by=["Smoliv", "Basic", "Smoliv"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=928,
    abilities=[
        Attack(
            title="Nutrients",
            game_text="Heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=heal_attack(30),
        ),
        Attack(
            title="Spray Fluid",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)