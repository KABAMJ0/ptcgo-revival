from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6afaf4d-e452-5944-8f2b-915f164e9e3e",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic", "Karrablast"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Ability(
            title="Stimulated Evolution",
            game_text="If you have Shelmet in play, this Pok\u00e9mon can evolve during your first turn or the turn you play it.",
            effect=unimplemented,
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)