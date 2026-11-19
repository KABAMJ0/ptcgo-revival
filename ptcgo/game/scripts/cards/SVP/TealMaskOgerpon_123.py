from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per

card = PokemonCardDef(
    guid="7842534f-7b06-5464-b1ad-bd39e94171ec",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerpon.Name",
    display_name="Teal Mask Ogerpon",
    searchable_by=["Teal Mask Ogerpon", "Basic", "TealMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1017,
    abilities=[
        Attack(
            title="Mountain Stroll",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ogre Comeback",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), per=20, base=20),
        ),
    ],
)