from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="079e4fc4-ee34-59fb-a68e-7116521789f5",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Ability(
            title="Wafting Heal",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may heal all damage from your Active Grass Pok\u00e9mon. If you healed any damage in this way, discard all Energy from that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)