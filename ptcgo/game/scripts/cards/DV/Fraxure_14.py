from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class GritPassive(Passive):
    """This Pokemon's own attacks do +40 while it is affected by a Special
    Condition (before applying Weakness and Resistance)."""

    def __init__(self, amount: int):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing) or calc.attacker is not holder:
            return
        if holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []:
            calc.amount += self.amount


card = PokemonCardDef(
    guid="3665cf9c-4cff-543d-8917-f1693321f78c",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    display_name="Fraxure",
    searchable_by=["Fraxure", "Stage 1", "Fraxure"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    family_id=610,
    abilities=[
        Ability(
            title="Grit",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, each of its attacks does 40 more damage (before applying Weakness and Resistance).",
            passive=GritPassive(40),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
