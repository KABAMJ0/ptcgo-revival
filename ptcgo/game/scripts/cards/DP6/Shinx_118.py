from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _lightning_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)

card = PokemonCardDef(
    guid="ee2f3acc-dc58-55cd-bed0-cc9782bfab3f",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    display_name="Shinx",
    searchable_by=["Shinx", "Basic", "Shinx"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=403,
    abilities=[
        Attack(
            title="Recharge",
            game_text="Search your deck for a Lightning Energy card attach it to Shinx. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(_lightning_energy, count=1, to_self=True),
        ),
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)