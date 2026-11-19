from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import condition_attack, snipe_attack

card = PokemonCardDef(
    guid="fcde684c-c4c1-5462-882f-821a89f2027c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuZekromGX.Name",
    display_name="Pikachu & Zekrom-GX",
    searchable_by=["Pikachu & Zekrom-GX", "Basic", "TAG TEAM", "GX", "PikachuZekromGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=248,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=25,
    abilities=[
        Attack(
            title="Full Blitz",
            game_text="Search your deck for up to 3 Lightning Energy cards and attach them to 1 of your Pokemon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=search_attach_energy(basic_energy_of("lightning"), count=3, distribute=False),
        ),
        Attack(
            title="Tag Bolt-GX",
            game_text="If this Pokemon has at least 3 extra Lightning Energy attached to it (in addition to this attack's cost), this attack does 170 damage to 1 of your opponent's Benched Pokemon. (Don't apply Weakness and Resistance for Benched Pokemon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            effect=condition_attack(
                damage=200,
                extra_energy=(3, PokemonTypes.LIGHTNING, snipe_attack(170, count=1)),
            ),
        ),
    ],
)