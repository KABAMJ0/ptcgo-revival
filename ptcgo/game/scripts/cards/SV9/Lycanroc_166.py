from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per

card = PokemonCardDef(
    guid="f9b94fe0-beb0-5a2f-a2e2-f1fa8e6bff71",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1", "Lycanroc"],
    subtypes=["Stage 1"],
    collector_number=166,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Ability(
            title="Spike-Clad",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach up to 2 Spiky Energy cards from your discard pile to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Clamping Fangs",
            game_text="This attack does 40 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), per=40, base=40),
        ),
    ],
)