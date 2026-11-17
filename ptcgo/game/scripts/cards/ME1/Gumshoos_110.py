from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90099ab3-e4f9-5618-9bb6-fc4bfef06307",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name",
    display_name="Gumshoos",
    searchable_by=["Gumshoos", "Stage 1", "Gumshoos"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Ability(
            title="Evidence Gathering",
            game_text="Once during your turn, you may use this Ability. Switch a card from your hand with the top card of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)