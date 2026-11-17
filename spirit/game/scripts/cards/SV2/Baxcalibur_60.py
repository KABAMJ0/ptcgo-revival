from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b89db57b-9a9c-5d33-80b2-7d0360b7a18e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baxcalibur.Name",
    display_name="Baxcalibur",
    searchable_by=["Baxcalibur", "Stage 2", "Baxcalibur"],
    subtypes=["Stage 2"],
    collector_number=60,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arctibax.Name",
    family_id=996,
    abilities=[
        Ability(
            title="Super Cold",
            game_text="As often as you like during your turn, you may attach a Basic Water Energy card from your hand to 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Buster Tail",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)