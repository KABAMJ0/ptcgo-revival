from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn, attacker_is_basic

card = PokemonCardDef(
    guid="bd2dc37f-c9d9-54d3-b396-ab8e1254d1fb",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivernex.Name",
    display_name="Noivern ex",
    searchable_by=["Noivern ex", "Stage 1", "ex", "Noivernex"],
    subtypes=["Stage 1", "ex"],
    collector_number=220,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Covert Flight",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_basic()),
        ),
        Attack(
            title="Dominating Echo",
            game_text="During your opponent's next turn, they can't play any Special Energy or Stadium cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=140,
            effect=unimplemented,
        ),
    ],
)