from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7bf7e1e8-cf0a-575d-9463-3a36516c3acf",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirgeex.Name",
    display_name="Skeledirge ex",
    searchable_by=["Skeledirge ex", "Stage 2", "ex", "Skeledirgeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=272,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Vitality Song",
            game_text="Heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=heal_targets(30, scope="each_own"),
        ),
        Attack(
            title="Burning Voice",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=270,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)