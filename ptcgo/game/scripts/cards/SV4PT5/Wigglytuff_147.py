from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d88ca522-f66b-5735-a96a-859e4a2dda18",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=147,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Ability(
            title="Balloon Therapy",
            game_text="Once during your turn, you may attach a Therapeutic Energy card from your hand to 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)