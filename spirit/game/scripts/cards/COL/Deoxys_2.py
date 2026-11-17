from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e004985-40ee-54f0-9ba5-dcf904cf40c4",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="COL",
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