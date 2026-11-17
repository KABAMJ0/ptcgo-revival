from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="52692a5e-31c2-5da1-b14b-b3f734510433",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Transformative Start",
            game_text="Once during your first turn, if this Pok\u00e9mon is in the Active Spot, you may search your deck and choose a Basic Pok\u00e9mon you find there, except any Ditto. If you do, discard this Pok\u00e9mon and all attached cards, and put the chosen Pok\u00e9mon in its place. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Splup",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)