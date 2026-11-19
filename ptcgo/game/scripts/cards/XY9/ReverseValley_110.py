from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.passives_common import (
    pokemon_of_types, takes_less_passive, team_damage_boost_passive, team_of_types,
)

card = StadiumCardDef(
    guid="4243938d-79db-5a5e-889c-d38432a88f37",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReverseValley.Name",
    display_name="Reverse Valley",
    searchable_by=["Reverse Valley", "Stadium"],
    subtypes=["Stadium"],
    collector_number=110,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    faces={
        "metal-less": {"passive": takes_less_passive(
            10, protects=team_of_types(PokemonTypes.METAL.value))},
        "darkness-more": {"passive": team_damage_boost_passive(
            10, attacker_pred=pokemon_of_types(PokemonTypes.DARKNESS.value))},
    },
    face_labels={
        "metal-less": "This side's Metal Pokemon take 10 less",
        "darkness-more": "This side's Darkness attacks do 10 more",
    },
)
