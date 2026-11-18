from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="727a83e6-723a-5668-b890-1437a78e0cf5",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    display_name="Mewtwo-EX",
    searchable_by=["Mewtwo-EX", "Basic", "EX", "MewtwoEX"],
    subtypes=["Basic", "EX"],
    collector_number=52,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Absorption",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Regeneration",
            game_text="Heal 60 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=heal_attack(60),
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)