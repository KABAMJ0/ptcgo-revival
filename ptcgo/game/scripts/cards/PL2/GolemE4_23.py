from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="e5b9cfd6-cf53-5de2-9425-14e6381c11ab",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GolemE4.Name",
    display_name="Golem E4",
    searchable_by=["Golem E4", "Basic", "SP", "GolemE4"],
    subtypes=["Basic", "SP"],
    collector_number=23,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=76,
    abilities=[
        Attack(
            title="Rage",
            game_text="Does 20 damage plus 10 more damage for each damage counter on Golem GL.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Double-edge",
            game_text="Golem E4 does 60 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=recoil_attack(60, damage=0),
        ),
    ],
)