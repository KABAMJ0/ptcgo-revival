from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0ff881ed-f108-5bce-a959-ae4dbd3ea20b",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "Tera", "ex", "Greninjaex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=214,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Shinobi Blade",
            game_text="You may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=170,
            effect=unimplemented,
        ),
        Attack(
            title="Mirage Barrage",
            game_text="Discard 2 Energy from this Pok\u00e9mon. This attack does 120 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)