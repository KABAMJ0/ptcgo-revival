from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2563949e-43b4-5b5f-8e9b-65c381a81e00",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Prime", "Raichu"],
    subtypes=["Stage 1", "Prime"],
    collector_number=83,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Voltage Increase",
            game_text="As often as you like during your turn (before your attack), you may move a Lightning Energy attached to 1 of your Pok\u00e9mon to Raichu. This power can't be used if Raichu is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Mega Thunderbolt",
            game_text="Discard all Energy attached to Raichu.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)