from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class KabutoArmorPassive(Passive):
    """Attack damage on Kabuto is halved and rounded down to the nearest 10,
    applied after Weakness and Resistance. Works against its own attacks too."""

    def modify_damage_taken(self, calc, carrier):
        if not calc.is_attack or calc.target is not carrier_pokemon(carrier):
            return
        if calc.target.get_attribute(AttrID.SPECIAL_CONDITIONS) or []:
            return
        calc.amount = ((calc.amount // 2) // 10) * 10


card = PokemonCardDef(
    guid="6b8753f4-e288-5867-85f5-72f18736d5b5",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Stage 1", "Kabuto"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Kabuto Armor",
            game_text="Whenever an attack (even your own) does damage to Kabuto (after applying Weakness and Resistance), that attack does only half the damage to Kabuto (rounded down to the nearest 10). (Any other effects of attacks still happen.) This power stops working while Kabuto is affected by a Special Condition.",
            passive=KabutoArmorPassive(),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)