from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.passives_common import opponent_retreat_tax_passive


card = PokemonCardDef(
    guid="981f6ddf-f836-5d41-87d6-ae8b6c3f6ec7",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name",
    display_name="Alolan Dugtrio",
    searchable_by=["Alolan Dugtrio", "Stage 1", "AlolanDugtrio"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Tangling Hair",
            game_text="Your opponent's Active Pok\u00e9mon's Retreat Cost is Colorless more.",
            passive=opponent_retreat_tax_passive(1, active_only=True),
        ),
        Attack(
            title="Dig Under",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(50, pool="any", count=1, apply_modifiers=False),
        ),
    ],
)