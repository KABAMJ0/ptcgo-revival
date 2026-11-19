from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="fc534927-b139-5431-b6c3-2d722cd7b3fb",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MLatiosEX.Name",
    display_name="M Latios-EX",
    searchable_by=["M Latios-EX", "MEGA", "EX", "MLatiosEX"],
    subtypes=["MEGA", "EX"],
    collector_number=102,
    set_code="XY6",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosEX.Name",
    family_id=381,
    abilities=[
        Attack(
            title="Sonic Ace",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=self_energy_discard_attack(count=2, before_damage=True, also=snipe_attack(120, pool="any", count=1)),
        ),
    ],
)