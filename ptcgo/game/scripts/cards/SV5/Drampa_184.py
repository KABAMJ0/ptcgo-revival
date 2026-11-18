from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8e78e48d-7a3c-5143-af60-2be8c58abc59",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=184,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Raging Cannon",
            game_text="If all of your Benched Pok\u00e9mon have at least 1 damage counter on them, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)