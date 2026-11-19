from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="a9db7dca-dd3d-5d69-b9a8-f4aaafc13401",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=203,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=381,
    abilities=[
        Attack(
            title="Skill Dive",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(50, pool="any", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)