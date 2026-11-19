from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="ad30ccbc-8d0c-5dbd-bc66-71031b319d70",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic", "PaldeanTauros"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=128,
    abilities=[
        Attack(
            title="Raging Charge",
            game_text="This attack does 40 damage for each of your Pok\u00e9mon that has \"Tauros\" in its name that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=recoil_attack(20),
        ),
    ],
)