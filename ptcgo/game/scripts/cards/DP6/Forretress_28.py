from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="53c33965-c3cf-5745-8174-3c3639585c87",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Ability(
            title="Iron Shell",
            game_text="Whenever you attach a basic Energy card from your hand to Forretress (excluding effects of attacks), you may flip a coin. If tails, put 2 damage counters on each Pok\u00e9mon (both yours and your opponent's) (excluding any Forretress).",
            effect=unimplemented,
        ),
        Attack(
            title="Explosion",
            game_text="Forretress does 40 damage to itself.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=recoil_attack(40),
        ),
    ],
)