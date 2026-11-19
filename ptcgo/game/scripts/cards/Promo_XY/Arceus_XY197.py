from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84a75418-085b-55d4-9836-602f88d5a80a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    display_name="Arceus",
    searchable_by=["Arceus", "Basic", "Arceus"],
    subtypes=["Basic"],
    collector_number=197,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Type Switch",
            game_text="Choose Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness, Metal, Fairy, or Dragon type. Until the end of your next turn, this Pok\u00e9mon is that type.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)