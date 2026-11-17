from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f1abf5cb-41fc-50ee-87cf-89bf3e0e940e",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "Tera", "ex", "Greninjaex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=106,
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