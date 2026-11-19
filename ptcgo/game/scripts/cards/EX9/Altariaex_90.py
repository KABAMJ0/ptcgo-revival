from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import Passive
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

class MistPassive(Passive):
    """Attacks from any Stage 2 Evolution (either side) do 30 less to the carrier."""

    def modify_damage_taken(self, calc, carrier):
        from ptcgo.game.session.passives import carrier_pokemon
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.target:
            return
        attacker = calc.attacker
        if attacker is not None and attacker.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value:
            calc.amount = max(0, calc.amount - 30)

card = PokemonCardDef(
    guid="2cec06e8-f5c6-58e6-846c-fd551c107445",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altariaex.Name",
    display_name="Altaria ex",
    searchable_by=["Altaria ex", "Stage 1", "ex", "Altariaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=90,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Mist",
            game_text="Any damage done to Altaria ex by attacks from Stage 2 Evolved Pok\u00e9mon (both yours and your opponent's) is reduced by 30 (after applying Weakness and Resistance).",
            effect=None,
            passive=MistPassive(),
        ),
        Attack(
            title="Dive",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Dragon Mist",
            game_text="This attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ignore_modifier_attack(ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)