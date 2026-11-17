from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb1a8cff-843c-564a-b54f-81141e61219e",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1", "Toxicroak"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Clean Hit",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)