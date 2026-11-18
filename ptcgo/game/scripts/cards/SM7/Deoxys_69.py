from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="36a2223f-bac5-5644-acd2-5d62983686ee",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Attack(
            title="Teleportation Burst",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Spear Dive",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(50, pool="any", count=1, apply_modifiers=False),
        ),
    ],
)