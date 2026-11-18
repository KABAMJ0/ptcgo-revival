from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ce77d2c-51a7-55b5-84b4-8846e1fbb668",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2", "Walrein"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Frigid Fangs",
            game_text="During your opponent's next turn, Pok\u00e9mon that have 2 or less Energy attached can't attack. (This includes new Pok\u00e9mon that come into play.)",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.WATER: 2},
            damage=170,
            effect=unimplemented,
        ),
    ],
)