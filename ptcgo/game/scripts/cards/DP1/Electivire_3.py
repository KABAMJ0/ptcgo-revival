from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5214707c-7c51-55c8-8c4b-ef0fe61cbea1",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="DP1",
    rarity=Rarities.RareHolo,
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
            title="Intense Voltage",
            game_text="As often as you like during your turn (before your attack), if Elekid is anywhere under Electivire, you may move a Lightning Energy attached to your Pok\u00e9mon to Electivire. This power can't be used if Electivire is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="You may discard all Lightning Energy attached to Electivire. If you do, this attack's base damage is 120 instead of 60.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)