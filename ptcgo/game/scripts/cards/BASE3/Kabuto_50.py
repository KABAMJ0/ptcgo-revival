from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import Passive, carrier_pokemon


class _KabutoArmor(Passive):
    """An attack that damages the holder (even its owner's own) does half that
    damage, rounded down to the nearest 10; off while afflicted."""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not calc.is_attack or calc.target is not holder:
            return
        if holder.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return
        calc.amount = (calc.amount // 2 // 10) * 10


_kabuto_armor = _KabutoArmor()

card = PokemonCardDef(
    guid="3061cd69-77ed-5bf8-8af4-74fbac8ef597",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Stage 1", "Kabuto"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="BASE3",
    rarity=Rarities.Common,
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
            game_text="Whenever an attack (even your own) does damage to Kabuto (after applying Weakness and Resistance), that attack does half the damage to Kabuto (rounded down to the nearest 10). (Any other effects of attacks still happen.) This power stops working while Kabuto is Asleep, Confused, or Paralyzed.",
            passive=_kabuto_armor,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)