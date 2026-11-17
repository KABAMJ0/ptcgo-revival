from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ef33f9d-5e94-5d4e-8eea-28e0944d48a0",
    key="COL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="COL1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Attack(
            title="Cell Storm",
            game_text="Discard 2 Psychic Energy attached to Deoxys and remove 6 damage counters from Deoxys.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            effect=unimplemented,
        ),
    ],
)