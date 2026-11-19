from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.support_common import switch_self_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a52fef3a-3ff7-5829-9f46-2269f4eb7e19",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleV.Name",
    display_name="Orbeetle V",
    searchable_by=["Orbeetle V", "Basic", "V", "OrbeetleV"],
    subtypes=["Basic", "V"],
    collector_number=12,
    set_code="SWSH11TG",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=826,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Mysterious Wave",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=50),
        ),
    ],
)