from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    count_energy,
    damage_per,
    discard_opponent_energy_attack,
)

card = PokemonCardDef(
    guid="a58d58f8-c280-5a1a-9a3c-03b6790b962d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PrimarinaGX.Name",
    display_name="Primarina-GX",
    searchable_by=["Primarina-GX", "Stage 2", "GX", "PrimarinaGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=39,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    family_id=730,
    abilities=[
        Attack(
            title="Bubble Beat",
            game_text="This attack does 20 more damage times the amount of Water Energy attached to your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("mine", PokemonTypes.WATER), 20, base=10),
        ),
        Attack(
            title="Roaring Seas",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=discard_opponent_energy_attack(damage=120),
        ),
        Attack(
            title="Grand Echo-GX",
            game_text="Heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)