from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="755219e7-78af-5a3e-b8cd-3a386dd82034",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    display_name="Smoliv",
    searchable_by=["Smoliv", "Basic", "Smoliv"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SVP",
    rarity=Rarities.RarePromo,
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
            effect=heal_attack(30, target="choice"),
        ),
        Attack(
            title="Spray Fluid",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)