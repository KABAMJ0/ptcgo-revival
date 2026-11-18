from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="74e357c0-6a67-5df7-9044-48894e1264e6",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic", "Scyther"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Attack(
            title="Swords Dance",
            game_text="During your next turn, Scyther's Slash attack's base damage is 60 instead of 30.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)