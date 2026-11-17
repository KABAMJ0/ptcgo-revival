from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e857f98f-aeb7-57b7-a255-075d12c84ef5",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapultex.Name",
    display_name="Dragapult ex",
    searchable_by=["Dragapult ex", "Stage 2", "Tera", "ex", "Dragapultex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=160,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
        Attack(
            title="Phantom Dive",
            game_text="Put 6 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)