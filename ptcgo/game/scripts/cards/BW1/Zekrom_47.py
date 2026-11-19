from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack, damage_counters_on, damage_per

card = PokemonCardDef(
    guid="faf9ff1b-522e-51c2-b0f1-01b751fb5ff3",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic", "Zekrom"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Outrage",
            game_text="Does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=20),
        ),
        Attack(
            title="Bolt Strike",
            game_text="This Pok\u00e9mon does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=recoil_attack(40),
        ),
    ],
)