from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.passives_common import (
    bench_capacity_passive, pokemon_of_types, takes_less_passive,
)

card = StadiumCardDef(
    guid="77d73cc0-02bd-5f76-af1c-a81dfe223324",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParallelCity.Name",
    display_name="Parallel City",
    searchable_by=["Parallel City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=145,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    faces={
        "bench-three": {"passive": bench_capacity_passive(
            3, protects="team", trim_to="discard")},
        "grass-fire-water": {"passive": takes_less_passive(
            20, protects="each", attacker_side="team",
            attacker_pred=pokemon_of_types(
                PokemonTypes.GRASS.value, PokemonTypes.FIRE.value,
                PokemonTypes.WATER.value))},
    },
    face_labels={
        "bench-three": "This side has 3 Bench spaces",
        "grass-fire-water": "This side's Grass, Fire and Water attacks do 20 less",
    },
)
