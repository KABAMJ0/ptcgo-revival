from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bfad2777-0e65-5264-a477-88d5a7fd958e",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandyShocks.Name",
    display_name="Sandy Shocks",
    searchable_by=["Sandy Shocks", "Basic", "Ancient", "SandyShocks"],
    subtypes=["Basic", "Ancient"],
    collector_number=98,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=989,
    abilities=[
        Attack(
            title="Magnetic Burst",
            game_text="If you have 3 or more Energy in play, this attack does 70 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)