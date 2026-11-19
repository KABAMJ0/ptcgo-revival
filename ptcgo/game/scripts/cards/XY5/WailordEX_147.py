from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import cure_on_energy_attach
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="50dc6278-ac4d-51ba-aaed-dc851cb390e3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WailordEX.Name",
    display_name="Wailord-EX",
    searchable_by=["Wailord-EX", "Basic", "EX", "WailordEX"],
    subtypes=["Basic", "EX"],
    collector_number=147,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=321,
    abilities=[
        Ability(
            title="Water Veil",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, remove all Special Conditions from it.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=cure_on_energy_attach(),
        ),
        Attack(
            title="High Breaching",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 5},
            damage=120,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)