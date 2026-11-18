from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="08a98e17-f90d-5794-9d64-fccd28bf631a",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Thumpalanche",
            game_text="Discard the top 5 cards of your deck. This attack does 80 damage for each Pok\u00e9mon with a Retreat Cost of exactly 4 that you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)