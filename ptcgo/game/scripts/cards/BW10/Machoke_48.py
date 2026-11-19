from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _at_ten_hp(ctx) -> bool:
    attacker = ctx.attacker
    return attacker is not None and attacker.get_attribute(AttrID.HP, 0) == 10


card = PokemonCardDef(
    guid="ac711040-4d92-56bf-9131-4c9f24684e65",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Last-Chance Chop",
            game_text="If this Pok\u00e9mon's remaining HP is 10, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_at_ten_hp, 70),
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)