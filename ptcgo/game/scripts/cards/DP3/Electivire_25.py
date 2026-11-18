from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6888338c-bc28-547d-a6bd-0382d4874328",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Ability(
            title="Motor Drive",
            game_text="Once during your turn (before your attack), you may search your discard pile for a Lightning Energy card and attach it to Electivire. This power can't be used if Electivire is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy attached to Electivire. Flip a coin for each Lightning Energy you discarded. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)