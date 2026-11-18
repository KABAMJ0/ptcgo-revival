from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="283362c0-3e45-58a5-8242-6691e1ebfbd4",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baxcalibur.Name",
    display_name="Baxcalibur",
    searchable_by=["Baxcalibur", "Stage 2", "Baxcalibur"],
    subtypes=["Stage 2"],
    collector_number=130,
    set_code="SV4PT5",
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