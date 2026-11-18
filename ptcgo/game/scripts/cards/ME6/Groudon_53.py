from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="240ffeee-29a6-5faa-86f9-381ddc96a521",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="ME6",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Brutal Lands",
            game_text="If a Stadium that has \"Legendary\" in its name is in play, this attack does 170 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)